import Alert from './Alert.vue'

export default {
    /**
     * 每个插件都有的install方法，用于安装插件
     * @param {Object} Vue - Vue类
     * @param {Object} [pluginOptions] - 插件安装配置
     */
    install(Vue, pluginOptions = {}) {
        // 创建"子类"方便挂载
        const VueAlert = Vue.extend(Alert)
        let alert = null

        /**
         * 初始化并显示alert
         * @returns {Promise} Promise实例
         */
        function $alert(content, time) {
            content = content || '';
            time = time;
            return new Promise((resolve) => {
                // 第一次调用
                if (!alert) {
                    alert = new VueAlert()
                    // 手动创建一个未挂载的实例
                    alert.$mount()
                    // 挂载
                    document.querySelector(pluginOptions.container || 'body').appendChild(alert.$el)
                }
                // 显示alert
                alert.show(content, time, () => { resolve() })

            })
        }
        // 定义关闭alert方法
        $alert.end = (noAnimate = false) => {
            return new Promise((resolve) => {
                if (!alert || !alert.isShow) {
                    resolve()
                    return
                }
                // 判断是否在关闭时需要动画
                if (noAnimate) {
                    // 默认只在此次行为下移除动画,之后的行为仍有动画
                    alert.removeAnimate().then(() => {
                        alert.opemAnimate()
                    })
                }

                alert.hide()
            })
        }

        Vue.alert = Vue.prototype.$alert = $alert
    },
}
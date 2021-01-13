<template>
    <transition :name="animateName">
        <div class="alerts" v-show="isShow">
            <div class="alerts-img">
                <div class="alerts-img-txt">{{content}}</div>
            </div>
        </div>
    </transition>
</template>
<script type="text/babel">
export default {
    data() {
        return {
            content: "",
            isShow: false,
            hasAnimate: true
        };
    },
    computed: {
        /**
         * 动画效果样式，没有返回空
         * @return {String} 样式
         */
        animateName() {
            return this.hasAnimate ? "opacity" : "";
        }
    },
    methods: {
        /**
         * 开启动画效果
         */
        opemAnimate() {
            this.hasAnimate = true;
        },
        /**
         * 去除动画效果
         * @return {Promise} 返回promise
         */
        removeAnimate() {
            return new Promise(resolve => {
                this.hasAnimate = false;
                resolve();
            });
        },
        /**
         * 显示动画loading
         */
        show(content, time, callback) {
            time = time || 1.5;
            this.content = content;
            this.isShow = true;
            setTimeout(() => {
                this.hide();
                "function" == typeof callback && callback();
            }, 1000 * time);
        },
        /**
         * 隐藏动画loading
         */
        hide() {
            this.isShow = false;
        }
    }
};
</script>

<style lang="scss" scoped>
.alerts {
    position: fixed;
    z-index: 9999999;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    background: transparent;

    &-img {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate3d(-50%, -50%, 0);
        background-color: rgba(0, 0, 0, 0.6);
        color: #fff;
        padding: 0.48rem 0.5rem;
        border-radius: 0.1rem;
        text-align: center;

        &-txt {
            font-size: 0.34rem;
        }
    }

    &-img img {
        width: 0.7rem;
        margin-bottom: 0.1rem;
    }

    &-loader {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate3d(-50%, -50%, 0);
        display: none;

        &-dot {
            width: 0.23rem;
            height: 0.23rem;
            background: #3ac;
            border-radius: 100%;
            display: inline-block;
            animation: slide 1s infinite;
            margin-right: 0.2rem;

            // for index in (1 .. 5) {
            //     &:nth-child({index}) {
            //         animation-delay: 0.2 + 0.1s * index;
            //         // background green(#ce2424, (50 * index))
            //         background: lighten(#ce2424, (index * 6));
            //     }
            // }
        }
    }
}

@keyframes slide {
    0% {
        transform: scale(1);
    }

    50% {
        opacity: 0.3;
        transform: scale(2);
    }

    100% {
        transform: scale(1);
    }
}

.opacity {
    &-enter-active, &-leave-active {
        transition: all 0.6s;
    }

    &-enter, &-leave-active {
        opacity: 0;
    }
}
</style>
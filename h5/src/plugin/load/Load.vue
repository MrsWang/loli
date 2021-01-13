<template>
	<div class="spinner" v-if="isShow">
		<div class="bounce1"></div>
		<div class="bounce2"></div>
		<div class="bounce3"></div>
	</div>
</template>
<script type="text/babel">
	export default {
		data() {
			return {
				isShow: false,
				hasAnimate: true,
			}
		},
		computed: {
			/**
			 * 动画效果样式，没有返回空
			 * @return {String} 样式
			 */
			animateName() {
				return this.hasAnimate ? 'opacity' : ''
			},
		},
		methods: {
			/**
			 * 开启动画效果
			 */
			opemAnimate() {
				this.hasAnimate = true
			},
			/**
			 * 去除动画效果
			 * @return {Promise} 返回promise
			 */
			removeAnimate() {
				return new Promise((resolve) => {
					this.hasAnimate = false;
					resolve()
				})
			},
			/**
			 * 显示动画loading
			 */
			show() {
				this.isShow = true
			},
			/**
			 * 隐藏动画loading
			 */
			hide() {
				this.isShow = false
			},
	}
	}
</script>

<style lang="scss" scoped>

.spinner {
	position: absolute;
	top:40%;
	left:50%;
	transform: translate(-50%,-40%);
	width: 70px;
	text-align: center;
}

.spinner > div {
	width: 18px;
	height: 18px;
	background-color: #FE6C7A;

	border-radius: 100%;
	display: inline-block;
	-webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
	animation: sk-bouncedelay 1.4s infinite ease-in-out both;
}

.spinner .bounce1 {
	-webkit-animation-delay: -0.32s;
	animation-delay: -0.32s;
}

.spinner .bounce2 {
	-webkit-animation-delay: -0.16s;
	animation-delay: -0.16s;
}

@-webkit-keyframes sk-bouncedelay {
	0%, 80%, 100% { -webkit-transform: scale(0) }
	40% { -webkit-transform: scale(1.0) }
}

@keyframes sk-bouncedelay {
	0%, 80%, 100% {
		-webkit-transform: scale(0);
		transform: scale(0);
	} 40% {
		  -webkit-transform: scale(1.0);
		  transform: scale(1.0);
	  }
}
</style>
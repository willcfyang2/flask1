<template>

    <div style="background-color: #161622;">

      <el-row :gutter="0">
        <el-col :span="12"  v-for="videoData in videoSrcList" :key="videoData">
          <div class="page">
            <video    
      :preload="preload" :poster="videoImg" :height="height" :width="width" align="center" :controls="controls"  :autoplay="autoplay">
        <source :src="videoData" type="video/mp4">
            </video>
        </div>
        </el-col>
      </el-row>

      
    </div>
</template>

<script>
import axios from 'axios'

  export default {
    data() {
    return {
      // videoSrc : 'http://127.0.0.1:5000/static/test.mp4',
      videoSrcList: [],
      playStatus: '',
      muteStatus: '',
      isMute: true,
      isPlay: false,
      width: '820', // 设置视频播放器的显示宽度（以像素为单位）
      height: '500', // 设置视频播放器的显示高度（以像素为单位）
      preload: 'auto', //  建议浏览器是否应在<video>加载元素后立即开始下载视频数据。
      controls: true, // 确定播放器是否具有用户可以与之交互的控件。没有控件，启动视频播放的唯一方法是使用autoplay属性或通过Player API。
      autoplay: ''
    }
  },
  methods:{
    getData(){
      let api = "api/video/read"
      axios.get(api).then((result)=>{
      this.videoSrcList = result.data.data
      console.log(this.videoSrcList)
    })
  }
  },
  mounted(){
      this.getData()

  },
  }

</script>

<style>
.page {
  margin-left : 40px;
  margin-top: 10px;
  margin-right: 10px;
  margin-bottom: 10px;
}



</style>

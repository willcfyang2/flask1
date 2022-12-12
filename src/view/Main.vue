<template>
    <div class="page">
        <el-row :gutter="30" justify="space-between">
            <el-col :span="6" v-for="(dataList) in picList" :key="dataList" v-bind:imgbase="dataList.image">
                <el-card :body-style="{ padding: '0px' }">
                    <img :src="dataList.image" class="image" alt="">
                    <div style="padding: 16px;">
                        <p>发表用户: {{dataList.user}}</p>
                        <p>图片标签: {{dataList.image_name}}</p>
                        <div class="bottom clearfix">
                        <!-- <time class="time">{{ currentDate }}</time> -->
                        <el-button type="text"  @click="getComment(dataList)" class="button">查看评论</el-button>
  
                            <el-dialog title="评论列表" :visible.sync="outerVisible">
                                <el-dialog width="30%" title="发表评论" :visible.sync="innerVisible" append-to-body>
                                    <el-form :model="numberValidateForm" ref="numberValidateForm" label-width="100px" class="demo-ruleForm">
                                        <el-form-item
                                            label="评论内容"
                                            prop="comment"
                                        >
                                            <el-input type="comment" v-model.number="numberValidateForm.comment" autocomplete="off"></el-input>
                                        </el-form-item>
                                        <el-form-item>
                                            <el-button type="primary" @click="submitForm()">commit</el-button>
                                            <el-button @click="resetForm">reset</el-button>
                                        </el-form-item>
                                    </el-form>
                                </el-dialog>
                                <el-table :data="commentList">
                                    <el-table-column property="username" label="用户" width="150" ></el-table-column>
                                    <el-table-column property="comment" label="评论" width=""  style="text-align: center;"></el-table-column>
                                </el-table>
                                <div slot="footer" class="dialog-footer">
                                <el-button @click="outerVisible = false">取 消</el-button>
                                <el-button type="primary" @click="innerVisible = true">发表评论</el-button>
                                </div>
                        </el-dialog>
                        <!-- <el-button type="text" class="button">查看评论</el-button> -->
                        </div>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>





<script>
import Card from '../components/Card'
import axios from 'axios'


export default {
    data() {
        return {
            outerVisible: false,
            innerVisible: false,
            picList : [],
            commentList : [],
            postComment : "",
            commit_pid : "",
            form: {
                source: '',
                target: '',
                num: '',
                begin: '',
                end: '',
                delivery: false,
            },
            formLabelWidth: '120px',
            isShow: false,
            chartPie: null,
            numberValidateForm: {
                comment: ''
            }
        }
    },
    components: {
        Card
    },
    methods: {
       getData(){
           let api = 'api/images/read'
           axios.get(api).then((result)=>{
           this.picList = result.data.data
           console.log(result)
        })
       },

       getComment(data){
            console.log(data)
            let pid = data.id
            let api = `api/comment?pid=${pid}`
            axios.get(api).then((result)=>{
            this.commentList = result.data.data
            this.commit_pid = pid
            console.log(result)
            console.log(this.commentList)
            this.outerVisible = true
        })
        
       },

       submitForm() {
        let _pid = this.commit_pid
        let _id = this.$store.state.token
        let api = 'api/comment/create'
        let parm = `pid=${_pid}&uid=${_id}&text=${this.numberValidateForm.comment}`
        console.log(_id)
        let valid = this.numberValidateForm.comment
        if (valid) {
            axios.post(api, parm).then((result)=>{
           this.picList = result.data.data
           console.log(result)
           this.commit_pid = ''
        //    this.getData()

            })
        } else {
        console.log('error submit!!');
        }
      },
      resetForm() {
        this.numberValidateForm.comment = ""
      }
    },
      
    mounted(){
        this.getData()

    },
}
</script>

<style>
.list-item {
    display: inline-block;
    margin-right: 10px;
}

.list-enter-active,
.list-leave-active {
    transition: all 1s;
}

.list-enter,
.list-leave-to
{
    opacity: 0;
    transform: translateY(30px);
}
.train{
    min-height: 600px;
}
.loadingBox{
    text-align: center;
    margin-top:20px;
    margin-bottom:20px;
}
.el-pagination {
    text-align: center;
    /* font-size: 20px; */
}

.comment {
    text-align: center
}

.page {
    background: white;
}

#box ul{
		display: flex;
		flex-wrap: wrap;
        position: absolute;
        top: 220px;
	}
#box li{
		padding: 3px;
		list-style: none;
		margin-right: 15px;
		border: 1px solid #eee;
}
#box img{
		width: 200px;
		height: 150px;
}


  .time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: left;
  }

  .dig {
    padding: 0;
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
    
    margin-bottom: 8px;

    margin-top: 8px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
  .el-table .success-row {
    background: #f0f9eb;
  }
</style>

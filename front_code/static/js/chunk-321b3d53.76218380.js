(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-321b3d53"],{"1df9":function(e,t,r){"use strict";r("b233")},9614:function(e,t,r){"use strict";r.r(t);var s=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("div",{staticClass:"crumbs"},[r("el-breadcrumb",{attrs:{separator:"/"}},[r("el-breadcrumb-item",[r("i",{staticClass:"el-icon-lx-calendar"}),e._v(" 套件管理")]),r("el-breadcrumb-item",[e._v("编辑套件")])],1)],1),r("div",{staticClass:"container"},[r("div",{staticClass:"form-box"},[r("el-form",{ref:"form",attrs:{rules:e.rules,model:e.form,"label-width":"100px"}},[r("el-form-item",{attrs:{label:"套件名称",prop:"name",required:""}},[r("el-input",{attrs:{"suffix-icon":"el-icon-menu",clearable:""},on:{focus:function(t){return e.clearValidate("name")}},model:{value:e.form.name,callback:function(t){e.$set(e.form,"name",t)},expression:"form.name"}})],1),r("el-form-item",{attrs:{label:"选择项目",prop:"project_id",required:""}},[r("el-select",{attrs:{placeholder:"请选择"},on:{change:function(t){return e.getInterfacesByProjectID(e.form.project_id)}},model:{value:e.form.project_id,callback:function(t){e.$set(e.form,"project_id",t)},expression:"form.project_id"}},e._l(e.project_names,(function(e,t){return r("el-option",{key:t,attrs:{label:e.name,value:e.id}})})),1)],1),r("el-form-item",{attrs:{label:"选择接口",required:""}},[r("div",{staticClass:"drag-box"},[r("div",{staticClass:"drag-box-item"},[r("div",{staticClass:"item-title"},[e._v("待选接口")]),r("draggable",{attrs:{options:e.dragOptions},model:{value:e.unselected,callback:function(t){e.unselected=t},expression:"unselected"}},[r("transition-group",{staticClass:"item-ul",attrs:{tag:"div"}},e._l(e.unselected,(function(t){return r("div",{key:t.id,staticClass:"drag-list"},[e._v("\n                                        "+e._s(t.name)+"\n                                    ")])})),0)],1)],1),r("div",{staticClass:"drag-box-item"},[r("div",{staticClass:"item-title"},[e._v("已选接口")]),r("draggable",{attrs:{options:e.dragOptions},on:{change:function(t){return e.changeResult()}},model:{value:e.selected,callback:function(t){e.selected=t},expression:"selected"}},[r("transition-group",{staticClass:"item-ul",attrs:{tag:"div"}},e._l(e.selected,(function(t){return r("div",{key:t.id,staticClass:"drag-list"},[e._v("\n                                        "+e._s(t.name)+"\n                                    ")])})),0)],1)],1)])]),r("el-form-item",[r("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.onSubmit("form")}}},[e._v("提交")]),r("el-button",{on:{click:function(t){return e.resetForm("form")}}},[e._v("取消")])],1)],1)],1)])])},n=[],a=(r("7f7f"),r("7618")),i=r("b76a"),o=r.n(i),c=r("4ec3"),l={beforeRouteEnter:function(e,t,r){r((function(e){e.current_testsuite_id=e.$route.params.id,e.getTestSuiteDetail()})),r()},beforeRouteUpdate:function(e,t,r){this.current_testsuite_id=e.params.id,this.getTestSuiteDetail(),r()},name:"baseform",data:function(){return{current_testsuite_id:null,form:{name:"",project_id:"",include:"[]"},rules:{name:[{required:!0,message:"请输入套件名称",trigger:"blur"}],project_id:[{required:!0,message:"请选择所属项目",trigger:"blur"}]},project_names:[],dragOptions:{animation:120,scroll:!0,group:"sortlist",ghostClass:"ghost-style"},unselected:[],selected:[]}},components:{draggable:o.a},created:function(){this.getProjectNames()},methods:{onSubmit:function(e){var t=this;this.$refs[e].validate((function(e){if(!e)return t.$message.error("参数有误"),!1;var r=t;Object(c["V"])(t.current_testsuite_id,t.form).then((function(e){t.$message.success("修改套件成功！"),setInterval((function(){r.$router.go()}),1e3)})).catch((function(e){"object"===Object(a["a"])(e)&&e.hasOwnProperty("name")?t.$message.error("套件名称已存在"):t.$message.error("服务器错误")}))}))},clearValidate:function(e){this.$refs["form"].clearValidate(e)},resetForm:function(e){this.$refs[e].resetFields()},getProjectNames:function(){var e=this;Object(c["F"])().then((function(t){e.project_names=t.data})).catch((function(e){that.$message.error("服务器错误")}))},removeHandle:function(e){console.log(e),this.$message.success("从 ".concat(e.from.id," 移动到 ").concat(e.to.id," "))},getInterfacesByProjectID:function(e){var t=this;Object(c["B"])(e).then((function(e){t.unselected=e.data.interfaces})).catch((function(e){that.$message.error("服务器错误")}))},changeResult:function(){for(var e=this.selected.length,t="[",r=0;r<e;r++)t+=r===e-1?this.selected[r].id+"]":this.selected[r].id+", ";0===e&&(t="[]"),this.form.include=t},getTestSuiteDetail:function(){var e=this;Object(c["A"])(this.current_testsuite_id).then((function(t){e.form.name=t.data.name,e.form.project_id=t.data.project_id,e.getInterfacesByProjectID(e.form.project_id),e.form.include=t.data.include})).catch((function(t){e.$message.error("服务器错误")}))}}},u=l,d=(r("1df9"),r("2877")),m=Object(d["a"])(u,s,n,!1,null,"6f08f646",null);t["default"]=m.exports},b233:function(e,t,r){}}]);
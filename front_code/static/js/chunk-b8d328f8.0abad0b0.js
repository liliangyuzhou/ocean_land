(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-b8d328f8"],{"4ec3":function(e,t,n){"use strict";n.d(t,"D",(function(){return o})),n.d(t,"G",(function(){return c})),n.d(t,"k",(function(){return s})),n.d(t,"j",(function(){return u})),n.d(t,"E",(function(){return l})),n.d(t,"q",(function(){return f})),n.d(t,"v",(function(){return d})),n.d(t,"d",(function(){return p})),n.d(t,"F",(function(){return h})),n.d(t,"x",(function(){return g})),n.d(t,"M",(function(){return b})),n.d(t,"h",(function(){return m})),n.d(t,"g",(function(){return y})),n.d(t,"i",(function(){return v})),n.d(t,"C",(function(){return _})),n.d(t,"p",(function(){return k})),n.d(t,"u",(function(){return w})),n.d(t,"c",(function(){return D})),n.d(t,"L",(function(){return j})),n.d(t,"S",(function(){return M})),n.d(t,"s",(function(){return z})),n.d(t,"f",(function(){return V})),n.d(t,"A",(function(){return $})),n.d(t,"V",(function(){return x})),n.d(t,"O",(function(){return S})),n.d(t,"B",(function(){return H})),n.d(t,"R",(function(){return T})),n.d(t,"r",(function(){return q})),n.d(t,"l",(function(){return O})),n.d(t,"Q",(function(){return I})),n.d(t,"e",(function(){return R})),n.d(t,"N",(function(){return C})),n.d(t,"z",(function(){return E})),n.d(t,"U",(function(){return N})),n.d(t,"K",(function(){return B})),n.d(t,"H",(function(){return P})),n.d(t,"I",(function(){return F})),n.d(t,"J",(function(){return L})),n.d(t,"m",(function(){return J})),n.d(t,"n",(function(){return W})),n.d(t,"a",(function(){return G})),n.d(t,"y",(function(){return K})),n.d(t,"T",(function(){return A})),n.d(t,"w",(function(){return U})),n.d(t,"o",(function(){return Q})),n.d(t,"t",(function(){return X})),n.d(t,"b",(function(){return Y})),n.d(t,"P",(function(){return Z}));var a=n("bc3a"),r=n.n(a),i="http://106.14.220.57:8000",o=function(e){return r.a.post("".concat(i,"/user/login/"),e)},c=function(e){return r.a.post("".concat(i,"/user/register/"),e)},s=function(e){return r.a.get("".concat(i,"/user/")+e+"/count/")},u=function(e){return r.a.get("".concat(i,"/user/")+e+"/count/")},l=function(e){return r.a.get("".concat(i,"/projects/?page=")+e.page+"&size="+e.size)},f=function(e){return r.a.delete("".concat(i,"/projects/")+e+"/")},d=function(e,t){return r.a.put("".concat(i,"/projects/")+e+"/",t)},p=function(e){return r.a.post("".concat(i,"/projects/"),e)},h=function(){return r.a.get("".concat(i,"/projects/names/"))},g=function(){return r.a.get("".concat(i,"/envs/names/"))},b=function(e,t){return r.a.post("".concat(i,"/projects/")+e+"/run/",{env_id:t})},m=function(e){return r.a.get("".concat(i,"/debugtalks/?page=")+e.page+"&size="+e.size)},y=function(e){return r.a.get("".concat(i,"/debugtalks/")+e+"/")},v=function(e,t){return r.a.put("".concat(i,"/debugtalks/")+e+"/",{debugtalk:t})},_=function(e){return r.a.get("".concat(i,"/interfaces/?page=")+e.page+"&size="+e.size)},k=function(e){return r.a.delete("".concat(i,"/interfaces/")+e+"/")},w=function(e,t){return r.a.put("".concat(i,"/interfaces/")+e+"/",t)},D=function(e){return r.a.post("".concat(i,"/interfaces/"),e)},j=function(e,t){return r.a.post("".concat(i,"/interfaces/")+e+"/run/",{env_id:t})},M=function(e){return r.a.get("".concat(i,"/testsuites/?page=")+e.page+"&size="+e.size)},z=function(e){return r.a.delete("".concat(i,"/testsuites/")+e+"/")},V=function(e){return r.a.post("".concat(i,"/testsuites/"),e)},$=function(e){return r.a.get("".concat(i,"/testsuites/")+e+"/")},x=function(e,t){return r.a.put("".concat(i,"/testsuites/")+e+"/",t)},S=function(e,t){return r.a.post("".concat(i,"/testsuites/")+e+"/run/",{env_id:t})},H=function(e){return r.a.get("".concat(i,"/projects/")+e+"/interfaces/")},T=function(e){return r.a.get("".concat(i,"/testcases/?page=")+e.page+"&size="+e.size)},q=function(e){return r.a.delete("".concat(i,"/testcases/")+e+"/")},O=function(e){return r.a.get("".concat(i,"/interfaces/")+e+"/configs/")},I=function(e){return r.a.get("".concat(i,"/interfaces/")+e+"/testcases/")},R=function(e){return r.a.post("".concat(i,"/testcases/"),e)},C=function(e,t){return r.a.post("".concat(i,"/testcases/")+e+"/run/",{env_id:t})},E=function(e){return r.a.get("".concat(i,"/testcases/")+e+"/")},N=function(e,t){return r.a.put("".concat(i,"/testcases/")+e+"/",t)},B=function(e){return r.a.get("".concat(i,"/reports/?page=")+e.page+"&size="+e.size)},P=function(e){return r.a.delete("".concat(i,"/reports/")+e+"/")},F=function(e){return r.a.get("".concat(i,"/reports/")+e+"/download/",{responseType:"blob"})},L=function(e){return r.a.get("".concat(i,"/reports/")+e+"/")},J=function(e){return r.a.get("".concat(i,"/configures/?page=")+e.page+"&size="+e.size)},W=function(e){return r.a.delete("".concat(i,"/configures/")+e+"/")},G=function(e){return r.a.post("".concat(i,"/configures/"),e)},K=function(e){return r.a.get("".concat(i,"/configures/")+e+"/")},A=function(e,t){return r.a.put("".concat(i,"/configures/")+e+"/",t)},U=function(e){return r.a.get("".concat(i,"/envs/?page=")+e.page+"&size="+e.size)},Q=function(e){return r.a.delete("".concat(i,"/envs/")+e+"/")},X=function(e,t){return r.a.put("".concat(i,"/envs/")+e+"/",t)},Y=function(e){return r.a.post("".concat(i,"/envs/"),e)},Z=function(){return r.a.get("".concat(i,"/summary/"))}},"5d58":function(e,t,n){e.exports=n("d8d6")},"67bb":function(e,t,n){e.exports=n("f921")},"6aa8":function(e,t,n){},7618:function(e,t,n){"use strict";n.d(t,"a",(function(){return c}));var a=n("67bb"),r=n.n(a),i=n("5d58"),o=n.n(i);function c(e){return c="function"===typeof r.a&&"symbol"===typeof o.a?function(e){return typeof e}:function(e){return e&&"function"===typeof r.a&&e.constructor===r.a&&e!==r.a.prototype?"symbol":typeof e},c(e)}},ad0c:function(e,t,n){"use strict";n.r(t);var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("div",{staticClass:"crumbs"},[n("el-breadcrumb",{attrs:{separator:"/"}},[n("el-breadcrumb-item",[n("i",{staticClass:"el-icon-lx-calendar"}),e._v(" 配置管理")]),n("el-breadcrumb-item",[e._v("新增配置")])],1)],1),n("div",{staticClass:"container"},[n("el-tabs",{attrs:{type:"border-card"}},[n("el-tab-pane",{attrs:{label:"请求头|全局变量"}},[n("el-tabs",{staticStyle:{margin:"0 0 0 10px"},model:{value:e.otherShow,callback:function(t){e.otherShow=t},expression:"otherShow"}},[n("el-tab-pane",{attrs:{label:"Headers",name:"first"}},[n("el-table",{staticClass:"h-b-e-a-style",attrs:{data:e.apiMsgData.header,size:"mini",stripe:"","show-header":!1,"row-style":{"background-color":"rgb(250, 250, 250)"}}},[n("el-table-column",{attrs:{property:"key",label:"Key","header-align":"center",minWidth:"100"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-input",{attrs:{size:"mini",placeholder:"key"},model:{value:t.row.key,callback:function(n){e.$set(t.row,"key",n)},expression:"scope.row.key"}})]}}])}),n("el-table-column",{attrs:{property:"value",label:"Value","header-align":"center",minWidth:"200"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-input",{attrs:{size:"mini",placeholder:"value"},model:{value:t.row.value,callback:function(n){e.$set(t.row,"value",n)},expression:"scope.row.value"}})]}}])}),n("el-table-column",{attrs:{property:"value",label:"操作","header-align":"center",width:"80"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-button",{attrs:{type:"danger",icon:"el-icon-delete",size:"mini"},nativeOn:{click:function(n){return e.delTableRow("header",t.$index)}}})]}}])})],1)],1),n("el-tab-pane",{attrs:{label:"全局变量",name:"second"}},[n("el-table",{staticClass:"h-b-e-a-style",attrs:{data:e.apiMsgData.globalVar,size:"mini",stripe:"","show-header":!1,"row-style":{"background-color":"rgb(250, 250, 250)"}}},[n("el-table-column",{attrs:{property:"key",label:"Key","header-align":"center",minWidth:"100"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-input",{attrs:{size:"mini",placeholder:"key"},model:{value:t.row.key,callback:function(n){e.$set(t.row,"key",n)},expression:"scope.row.key"}})]}}])}),n("el-table-column",{attrs:{label:"type","header-align":"center",width:"100"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-select",{attrs:{size:"mini"},model:{value:t.row.param_type,callback:function(n){e.$set(t.row,"param_type",n)},expression:"scope.row.param_type"}},e._l(e.paramTypes,(function(e){return n("el-option",{key:e,attrs:{value:e}})})),1)]}}])}),n("el-table-column",{attrs:{property:"value",label:"Value","header-align":"center",minWidth:"200"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-input",{attrs:{size:"mini",placeholder:"value"},model:{value:t.row.value,callback:function(n){e.$set(t.row,"value",n)},expression:"scope.row.value"}})]}}])}),n("el-table-column",{attrs:{property:"value",label:"操作","header-align":"center",width:"80"},scopedSlots:e._u([{key:"default",fn:function(t){return[n("el-button",{attrs:{type:"danger",icon:"el-icon-delete",size:"mini"},nativeOn:{click:function(n){return e.delTableRow("globalVar",t.$index)}}})]}}])})],1)],1)],1)],1)],1),n("el-row",[n("el-col",{attrs:{span:2}},[n("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.onSubmit()}}},[e._v("提交")])],1),n("el-col",{attrs:{span:2}},[n("el-button",{on:{click:function(t){return e.resetForm("form")}}},[e._v("取消")])],1)],1)],1),n("el-dialog",{attrs:{title:"创建配置",visible:e.editVisible,width:"28%",center:""},on:{"update:visible":function(t){e.editVisible=t}}},[n("el-form",{attrs:{"label-width":"120px"}},[n("el-form-item",{attrs:{label:"配置名称",required:""}},[n("el-input",{attrs:{clearable:""},model:{value:e.configure_name,callback:function(t){e.configure_name=t},expression:"configure_name"}})],1),n("el-form-item",{attrs:{label:"编写人员",required:""}},[n("el-input",{attrs:{clearable:""},model:{value:e.author,callback:function(t){e.author=t},expression:"author"}})],1),n("el-form-item",{attrs:{label:"选择项目",required:""}},[n("el-select",{attrs:{placeholder:"请选择"},on:{change:function(t){return e.getInterfacesByProjectID(e.selected_project_id)}},model:{value:e.selected_project_id,callback:function(t){e.selected_project_id=t},expression:"selected_project_id"}},e._l(e.project_names,(function(e,t){return n("el-option",{key:t,attrs:{label:e.name,value:e.id}})})),1)],1),n("el-form-item",{attrs:{label:"选择接口",required:""}},[n("el-select",{attrs:{placeholder:"请选择"},model:{value:e.selected_interface_id,callback:function(t){e.selected_interface_id=t},expression:"selected_interface_id"}},e._l(e.interfaces,(function(e,t){return n("el-option",{key:t,attrs:{label:e.name,value:e.id}})})),1)],1)],1),n("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:function(t){e.editVisible=!1}}},[e._v("取 消")]),n("el-button",{attrs:{type:"primary"},on:{click:e.saveEdit}},[e._v("确 定")])],1)],1)],1)},r=[],i=n("7618"),o=(n("c5f6"),n("4ec3")),c={name:"baseform",data:function(){return{editVisible:!1,apiMsgData:{id:null,name:"",header:[{key:null,value:null}],globalVar:[{key:null,value:null,param_type:"string"}]},bodyShow:"second",otherShow:"first",paramTypes:["string","int","float","boolean"],cell:Object(),project_names:[],selected_project_id:null,selected_interface_id:null,selected_configure_id:null,configure_name:null,author:"",interfaces:[],configures:[]}},created:function(){this.getProjectNames()},methods:{onSubmit:function(){this.selected_project_id=null,this.selected_interface_id=null,this.editVisible=!0},handleData1:function(e,t){for(var n=[],a=0;a<e.length;a++){var r=e[a].key;if(!r)return this.$message.error(t+"的key为空!"),[];var i=e[a].param_type,o=e[a].value;if("int"===i){if(!/^\d+$/.test(o))return this.$message.error(t+"不是整数int类型!"),[];o=Number(o)}else if("float"===i){if(!/^[+-]?\d+(\.\d+)?$/.test(o))return this.$message.error(t+"不是小数float类型!"),[];o=Number(o)}else if("boolean"===i)if(/^(true|True|TRUE|1|0)$/.test(o))o=!0;else{if(!/^(false|False|FALSE|0)$/.test(o))return this.$message.error(t+"不是布尔boolean类型!"),[];o=!1}var c={};c[r]=o,n.push(c)}return n},handleData2:function(e,t){for(var n={},a=0;a<e.length;a++){var r=e[a].key;if(!r)return this.$message.error(t+"的key为空!"),[];n[r]=e[a].value}return n},saveEdit:function(){var e=this;if(null!==this.configure_name)if(""!==this.author)if(null!==this.selected_project_id&&null!==this.selected_interface_id){var t={name:this.configure_name,interface:{project_id:this.selected_project_id,interface_id:this.selected_interface_id},author:this.author,request:{config:{name:this.configure_name,request:{}}}},n=this.apiMsgData.globalVar;if(n.splice(-1,1),0!==n.length){var a=this.handleData1(n,"全局变量variables");if(0===a.length)return;t.request.config["variables"]=a}var r=this.apiMsgData.header;if(r.splice(-1,1),0!==r.length){var c=this.handleData2(r,"请求头header");if(0===c.length)return;t.request.config.request["headers"]=c}t.request=JSON.stringify(t.request),Object(o["a"])(t).then((function(t){e.editVisible=!1;var n=e;e.$message.success("新增配置成功"),setInterval((function(){n.$router.go()}),1e3)})).catch((function(t){e.editVisible=!1,"object"===Object(i["a"])(t)&&t.hasOwnProperty("name")?(console.log(t),e.$message.error("配置名称已存在")):(console.log(t),e.$message.error("服务器错误"))}))}else this.$message.error("未选择所属项目或者接口!");else this.$message.error("编写人员名称不能为空!");else this.$message.error("配置名称不能为空!")},getProjectNames:function(){var e=this;Object(o["F"])().then((function(t){e.project_names=t.data})).catch((function(e){that.$message.error("服务器错误")}))},getInterfacesByProjectID:function(e){var t=this;Object(o["B"])(e).then((function(e){t.interfaces=e.data.interfaces})).catch((function(e){that.$message.error("服务器错误")}))},getConfTestcaseByInterfaceID:function(e){var t=this;Object(o["l"])(e).then((function(e){t.configures=e.data})).catch((function(e){that.$message.error("服务器错误")}))},delTableRow:function(e,t){"variable"===e?this.apiMsgData.variable.splice(t,1):"header"===e?this.apiMsgData.header.splice(t,1):"param"===e?this.apiMsgData.param.splice(t,1):"globalVar"===e?this.apiMsgData.globalVar.splice(t,1):"parameterized"===e?this.apiMsgData.parameterized.splice(t,1):"setupHooks"===e?this.apiMsgData.setupHooks.splice(t,1):"teardownHooks"===e&&this.apiMsgData.teardownHooks.splice(t,1)},addTableRow:function(e){"variable"===e?this.apiMsgData.variable.push({key:null,value:null,param_type:"string"}):"header"===e?this.apiMsgData.header.push({key:null,value:null}):"param"===e?this.apiMsgData.param.push({key:null,value:null}):"globalVar"===e?this.apiMsgData.globalVar.push({key:null,value:null,param_type:"string"}):"parameterized"===e?this.apiMsgData.parameterized.push({key:null,value:null}):"setupHooks"===e?this.apiMsgData.setupHooks.push({key:null}):"teardownHooks"===e&&this.apiMsgData.teardownHooks.push({key:null})},tempNum:function(e){this.temp_num=e},resetLine:function(){this.cell.style.height="18px"},showLine:function(e,t){this.cell=document.getElementById(e+t),this.cell.style.height=this.cell.scrollHeight+"px"},changeLine:function(){if(this.cell.style.height!==this.cell.scrollHeight+"px"){var e=parseInt(this.cell.style.height.substring(0,this.cell.style.height.length-2));e-this.cell.scrollHeight===2?this.cell.style.height=e-18+"px":this.cell.style.height=this.cell.scrollHeight+"px"}},querySearch:function(e,t){t(this.comparators)}},computed:{monitorHeader:function(){return this.apiMsgData.header},monitorGlobalVar:function(){return this.apiMsgData.globalVar}},watch:{monitorHeader:{handler:function(){0===this.apiMsgData.header.length&&this.addTableRow("header"),(this.apiMsgData.header[this.apiMsgData.header.length-1]["key"]||this.apiMsgData.header[this.apiMsgData.header.length-1]["value"])&&this.addTableRow("header")},deep:!0},monitorGlobalVar:{handler:function(){0===this.apiMsgData.globalVar.length&&this.addTableRow("globalVar"),(this.apiMsgData.globalVar[this.apiMsgData.globalVar.length-1]["key"]||this.apiMsgData.globalVar[this.apiMsgData.globalVar.length-1]["value"])&&this.addTableRow("globalVar")},deep:!0}}},s=c,u=(n("c60d"),n("2877")),l=Object(u["a"])(s,a,r,!1,null,"32fc0e12",null);t["default"]=l.exports},c60d:function(e,t,n){"use strict";n("6aa8")}}]);
(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-4ed631be"],{"4ec3":function(t,e,n){"use strict";n.d(e,"D",(function(){return i})),n.d(e,"G",(function(){return u})),n.d(e,"k",(function(){return o})),n.d(e,"j",(function(){return s})),n.d(e,"E",(function(){return l})),n.d(e,"q",(function(){return d})),n.d(e,"v",(function(){return f})),n.d(e,"d",(function(){return p})),n.d(e,"F",(function(){return g})),n.d(e,"x",(function(){return h})),n.d(e,"M",(function(){return b})),n.d(e,"h",(function(){return m})),n.d(e,"g",(function(){return _})),n.d(e,"i",(function(){return v})),n.d(e,"C",(function(){return z})),n.d(e,"p",(function(){return w})),n.d(e,"u",(function(){return C})),n.d(e,"c",(function(){return k})),n.d(e,"L",(function(){return x})),n.d(e,"S",(function(){return D})),n.d(e,"s",(function(){return j})),n.d(e,"f",(function(){return y})),n.d(e,"A",(function(){return S})),n.d(e,"V",(function(){return V})),n.d(e,"O",(function(){return O})),n.d(e,"B",(function(){return $})),n.d(e,"R",(function(){return T})),n.d(e,"r",(function(){return A})),n.d(e,"l",(function(){return J})),n.d(e,"Q",(function(){return R})),n.d(e,"e",(function(){return E})),n.d(e,"N",(function(){return q})),n.d(e,"z",(function(){return B})),n.d(e,"U",(function(){return F})),n.d(e,"K",(function(){return G})),n.d(e,"H",(function(){return H})),n.d(e,"I",(function(){return I})),n.d(e,"J",(function(){return K})),n.d(e,"m",(function(){return L})),n.d(e,"n",(function(){return M})),n.d(e,"a",(function(){return N})),n.d(e,"y",(function(){return P})),n.d(e,"T",(function(){return Q})),n.d(e,"w",(function(){return U})),n.d(e,"o",(function(){return W})),n.d(e,"t",(function(){return X})),n.d(e,"b",(function(){return Y})),n.d(e,"P",(function(){return Z}));var r=n("bc3a"),c=n.n(r),a="http://106.14.220.57:8000",i=function(t){return c.a.post("".concat(a,"/user/login/"),t)},u=function(t){return c.a.post("".concat(a,"/user/register/"),t)},o=function(t){return c.a.get("".concat(a,"/user/")+t+"/count/")},s=function(t){return c.a.get("".concat(a,"/user/")+t+"/count/")},l=function(t){return c.a.get("".concat(a,"/projects/?page=")+t.page+"&size="+t.size)},d=function(t){return c.a.delete("".concat(a,"/projects/")+t+"/")},f=function(t,e){return c.a.put("".concat(a,"/projects/")+t+"/",e)},p=function(t){return c.a.post("".concat(a,"/projects/"),t)},g=function(){return c.a.get("".concat(a,"/projects/names/"))},h=function(){return c.a.get("".concat(a,"/envs/names/"))},b=function(t,e){return c.a.post("".concat(a,"/projects/")+t+"/run/",{env_id:e})},m=function(t){return c.a.get("".concat(a,"/debugtalks/?page=")+t.page+"&size="+t.size)},_=function(t){return c.a.get("".concat(a,"/debugtalks/")+t+"/")},v=function(t,e){return c.a.put("".concat(a,"/debugtalks/")+t+"/",{debugtalk:e})},z=function(t){return c.a.get("".concat(a,"/interfaces/?page=")+t.page+"&size="+t.size)},w=function(t){return c.a.delete("".concat(a,"/interfaces/")+t+"/")},C=function(t,e){return c.a.put("".concat(a,"/interfaces/")+t+"/",e)},k=function(t){return c.a.post("".concat(a,"/interfaces/"),t)},x=function(t,e){return c.a.post("".concat(a,"/interfaces/")+t+"/run/",{env_id:e})},D=function(t){return c.a.get("".concat(a,"/testsuites/?page=")+t.page+"&size="+t.size)},j=function(t){return c.a.delete("".concat(a,"/testsuites/")+t+"/")},y=function(t){return c.a.post("".concat(a,"/testsuites/"),t)},S=function(t){return c.a.get("".concat(a,"/testsuites/")+t+"/")},V=function(t,e){return c.a.put("".concat(a,"/testsuites/")+t+"/",e)},O=function(t,e){return c.a.post("".concat(a,"/testsuites/")+t+"/run/",{env_id:e})},$=function(t){return c.a.get("".concat(a,"/projects/")+t+"/interfaces/")},T=function(t){return c.a.get("".concat(a,"/testcases/?page=")+t.page+"&size="+t.size)},A=function(t){return c.a.delete("".concat(a,"/testcases/")+t+"/")},J=function(t){return c.a.get("".concat(a,"/interfaces/")+t+"/configs/")},R=function(t){return c.a.get("".concat(a,"/interfaces/")+t+"/testcases/")},E=function(t){return c.a.post("".concat(a,"/testcases/"),t)},q=function(t,e){return c.a.post("".concat(a,"/testcases/")+t+"/run/",{env_id:e})},B=function(t){return c.a.get("".concat(a,"/testcases/")+t+"/")},F=function(t,e){return c.a.put("".concat(a,"/testcases/")+t+"/",e)},G=function(t){return c.a.get("".concat(a,"/reports/?page=")+t.page+"&size="+t.size)},H=function(t){return c.a.delete("".concat(a,"/reports/")+t+"/")},I=function(t){return c.a.get("".concat(a,"/reports/")+t+"/download/",{responseType:"blob"})},K=function(t){return c.a.get("".concat(a,"/reports/")+t+"/")},L=function(t){return c.a.get("".concat(a,"/configures/?page=")+t.page+"&size="+t.size)},M=function(t){return c.a.delete("".concat(a,"/configures/")+t+"/")},N=function(t){return c.a.post("".concat(a,"/configures/"),t)},P=function(t){return c.a.get("".concat(a,"/configures/")+t+"/")},Q=function(t,e){return c.a.put("".concat(a,"/configures/")+t+"/",e)},U=function(t){return c.a.get("".concat(a,"/envs/?page=")+t.page+"&size="+t.size)},W=function(t){return c.a.delete("".concat(a,"/envs/")+t+"/")},X=function(t,e){return c.a.put("".concat(a,"/envs/")+t+"/",e)},Y=function(t){return c.a.post("".concat(a,"/envs/"),t)},Z=function(){return c.a.get("".concat(a,"/summary/"))}},"53e8":function(t,e,n){},"9dfa":function(t,e,n){"use strict";n("53e8")},e6c3:function(t,e,n){"use strict";n.r(e);var r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"table"},[n("div",{staticClass:"crumbs"},[n("el-breadcrumb",{attrs:{separator:"/"}},[n("el-breadcrumb-item",[n("i",{staticClass:"el-icon-lx-calendar"}),t._v(" 配置管理")]),n("el-breadcrumb-item",[t._v("配置列表")])],1)],1),n("div",{staticClass:"container"},[n("div",{staticClass:"handle-box"},[n("el-button",{staticClass:"handle-del mr10",attrs:{type:"primary",icon:"el-icon-delete"},on:{click:t.delAll}},[t._v("批量删除")]),n("el-input",{staticClass:"handle-input mr10",attrs:{placeholder:"输入筛选关键词"},model:{value:t.select_word,callback:function(e){t.select_word=e},expression:"select_word"}})],1),n("el-table",{ref:"multipleTable",staticClass:"table",attrs:{data:t.data,border:"",stripe:""},on:{"selection-change":t.handleSelectionChange}},[n("el-table-column",{attrs:{type:"selection",width:"55",align:"center"}}),n("el-table-column",{attrs:{type:"index",label:"序号",width:"55",align:"center"}}),n("el-table-column",{attrs:{prop:"name",label:"配置名称",width:"250"}}),n("el-table-column",{attrs:{prop:"interface.project",label:"所属项目",width:"250"}}),n("el-table-column",{attrs:{prop:"interface.name",label:"所属接口",width:"250"}}),n("el-table-column",{attrs:{prop:"author",label:"编辑人员",width:"100",align:"center"}}),n("el-table-column",{attrs:{label:"操作",align:"center"},scopedSlots:t._u([{key:"default",fn:function(e){return[n("el-button",{attrs:{type:"text",icon:"el-icon-edit"},on:{click:function(n){return t.linkTo(e.row.id)}}},[t._v("编辑")]),n("el-button",{staticClass:"red",attrs:{type:"text",icon:"el-icon-delete"},on:{click:function(n){return t.handleDelete(e.$index,e.row)}}},[t._v("删除")])]}}])})],1),n("div",{staticClass:"pagination"},[n("el-pagination",{attrs:{background:"","page-sizes":[4,5,8,10,20],layout:"total, sizes, prev, pager, next, jumper",total:t.total_nums,"page-size":t.page_size},on:{"current-change":t.handleCurrentChange,"size-change":t.handleSizeChange}})],1)],1),n("el-dialog",{attrs:{title:"删除配置",visible:t.delVisible,width:"300px",center:""},on:{"update:visible":function(e){t.delVisible=e}}},[n("div",{staticClass:"del-dialog-cnt"},[t._v("删除不可恢复，是否确定删除？")]),n("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:function(e){t.delVisible=!1}}},[t._v("取 消")]),n("el-button",{attrs:{type:"primary"},on:{click:t.deleteRow}},[t._v("确 定")])],1)])],1)},c=[],a=(n("7f7f"),n("4ec3")),i={name:"basetable",data:function(){return{tableData:[],cur_page:1,page_size:10,total_nums:1,multipleSelection:[],select_word:"",del_list:[],editVisible:!1,delVisible:!1,runVisible:!1,form:{},idx:-1,id:-1}},created:function(){this.getData()},computed:{data:function(){var t=this;return this.tableData.filter((function(e){for(var n=!1,r=0;r<t.del_list.length;r++)if(e.name===t.del_list[r].name){n=!0;break}if(!n&&(e.name.indexOf(t.select_word)>-1||e.interface.project.indexOf(t.select_word)>-1||e.interface.name.indexOf(t.select_word)>-1||e.author.indexOf(t.select_word)>-1))return e}))}},methods:{handleCurrentChange:function(t){this.cur_page=t,this.getData()},handleSizeChange:function(t){this.page_size=t,this.getData()},getData:function(){var t=this;Object(a["m"])({page:this.cur_page,size:this.page_size}).then((function(e){t.tableData=e.data.results,t.cur_page=e.data.current_page_num||1,t.total_nums=e.data.count||1}))},search:function(){this.is_search=!0},handleDelete:function(t,e){this.idx=t,this.id=e.id,this.delVisible=!0},delAll:function(){var t=this,e=this.multipleSelection.length,n="";this.del_list=this.del_list.concat(this.multipleSelection);for(var r=0;r<e;r++)n+=this.multipleSelection[r].name+" ",delete_testcase(this.multipleSelection[r].id).then((function(t){})).catch((function(e){t.$message.error("服务器错误")}));this.$message.error("删除了"+n),this.multipleSelection=[]},handleSelectionChange:function(t){this.multipleSelection=t},deleteRow:function(){var t=this;Object(a["n"])(this.id).then((function(e){if(t.$message.success("删除成功"),t.delVisible=!1,t.tableData[t.idx].id===t.id)t.tableData.splice(t.idx,1);else for(var n=0;n<t.tableData.length;n++)if(t.tableData[n].id===t.id)return void t.tableData.splice(n,1)})).catch((function(e){t.$message.error("服务器错误")}))},linkTo:function(t){this.$router.push({path:"/configures_edit/".concat(t)})}}},u=i,o=(n("9dfa"),n("2877")),s=Object(o["a"])(u,r,c,!1,null,"f88ef53c",null);e["default"]=s.exports}}]);
(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-60b518af"],{"261d":function(t,e,a){"use strict";var i=a("7f53"),s=a.n(i);s.a},"7f53":function(t,e,a){},e180:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"full-screen"},[a("v-toolbar",{attrs:{fixed:"",dark:"",color:"primary"}},[a("v-icon",{on:{click:function(e){t.$router.go(-1)}}},[t._v("keyboard_backspace")]),a("v-toolbar-title",[t._v("d-DeViS")])],1),a("div",{staticClass:"visualization"},[a("div",{staticClass:"image-zoom"},[a("div",{staticClass:"component"},[a("original-image",{attrs:{title:"original prediction",hash:t.hash,digit:t.digit,"link-template":t.linkTemplate}}),a("br"),a("original-image",{attrs:{title:"prediction on modified features","waveform-title":"waveform, modified prediction",hash:t.hash2,digit:t.digit2,"link-template":t.linkTemplate}})],1)]),a("div",[a("h3",{attrs:{STYLE:"text-align: center"}},[t._v("LAYERS")]),a("v-tabs",{attrs:{"fixed-tabs":""},model:{value:t.activeLayer,callback:function(e){t.activeLayer=e},expression:"activeLayer"}},[t._l(3,function(e){return a("v-tab",{key:e},[t._v("\n          Layer "+t._s(e)+"\n        ")])}),a("v-tab",[t._v("All Layers")]),t._l(3,function(e){return a("v-tab-item",{key:e},[a("div",{staticClass:"title ma-4 text-uppercase",staticStyle:{"text-align":"center"}},[t._v("Original Prediction "+t._s(t.digit))]),a("sound-layer",{attrs:{"link-template":t.linkTemplate,hash:t.hash,"current-layer":e}}),a("div",{staticClass:"title ma-4 text-uppercase",staticStyle:{"text-align":"center"}},[t._v("Modified Prediction "+t._s(t.digit2))]),a("sound-layer",{attrs:{"link-template":t.linkTemplate,hash:t.hash2,"current-layer":e}})],1)}),a("v-tab-item",[a("div",{staticClass:"group-odd"},[a("div",{staticClass:"title ma-4 text-uppercase",staticStyle:{"text-align":"center"}},[t._v("Layer 1, Original Prediction "+t._s(t.digit))]),a("sound-layer",{attrs:{"link-template":t.linkTemplate,hash:t.hash,"current-layer":1}}),a("div",{staticClass:"title ma-4 text-uppercase",staticStyle:{"text-align":"center"}},[t._v("Layer 1, Modified Prediction "+t._s(t.digit2))]),a("sound-layer",{attrs:{"link-template":t.linkTemplate,hash:t.hash2,"current-layer":1}}),a("br")],1),a("v-divider"),a("br"),a("div",{staticClass:"group-even"},[a("div",{staticClass:"title ma-4 text-uppercase",staticStyle:{"text-align":"center"}},[t._v("Layer 2, Original Prediction "+t._s(t.digit2))]),a("sound-layer",{attrs:{"link-template":t.linkTemplate,hash:t.hash2,"current-layer":2}}),a("div",{staticClass:"title ma-4 text-uppercase",staticStyle:{"text-align":"center"}},[t._v("Layer 2, Modified Prediction "+t._s(t.digit))]),a("sound-layer",{attrs:{"link-template":t.linkTemplate,hash:t.hash,"current-layer":2}}),a("br")],1),a("v-divider"),a("br"),a("div",{staticClass:"group-odd"},[a("div",{staticClass:"title ma-4 text-uppercase",staticStyle:{"text-align":"center"}},[t._v("Layer 2, Original Prediction "+t._s(t.digit))]),a("sound-layer",{attrs:{"link-template":t.linkTemplate,hash:t.hash,"current-layer":3}}),a("div",{staticClass:"title ma-4 text-uppercase",staticStyle:{"text-align":"center"}},[t._v("Layer 3, Modified Prediction "+t._s(t.digit2))]),a("sound-layer",{attrs:{"link-template":t.linkTemplate,hash:t.hash2,"current-layer":3}})],1)],1)],2)],1)])],1)},s=[],l=(a("cadf"),a("551c"),a("097d"),a("b8c3")),r=a("373d"),n=a("987a"),c=a("b20c"),d=a("5047"),o=(console.log,{name:"VisualizeLayer",components:{layerComponent:l["a"],uploadForm:r["a"],originalImage:n["a"],soundLayer:c["a"]},created:function(){var t=localStorage.getItem("serverResponse"),e=localStorage.getItem("serverResponse2");t&&e?(t=JSON.parse(t),e=JSON.parse(e),this.digit=parseInt(t.data),this.digit2=parseInt(e.data),this.linkTemplate=d["a"].domain+t["link_template"],this.hash=t.hash,this.hash2=e.hash):alert("The model was not loaded successfully. Try uploading the file again.")},data:function(){return{activeLayer:0,digit:"",linkTemplate:"",hash:"",digit2:"",hash2:""}}}),p=o,h=(a("261d"),a("2877")),u=a("6544"),v=a.n(u),m=a("ce7e"),g=a("132d"),y=a("71a3"),f=a("c671"),k=a("fe57"),_=a("71d9"),b=a("2a7f"),x=Object(h["a"])(p,i,s,!1,null,"12f80b7c",null);x.options.__file="CompareModified.vue";e["default"]=x.exports;v()(x,{VDivider:m["a"],VIcon:g["a"],VTab:y["a"],VTabItem:f["a"],VTabs:k["a"],VToolbar:_["a"],VToolbarTitle:b["b"]})}}]);
//# sourceMappingURL=chunk-60b518af.19c10366.js.map
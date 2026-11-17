const V="ab-planner-v6";const C=V;const F=["./","index.html","manifest.webmanifest","icon-180.png","icon-192.png","icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(F)))});
self.addEventListener("message",e=>{if(e.data==="skip")self.skipWaiting()});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!=C).map(x=>caches.delete(x)))));self.clients.claim()});
self.addEventListener("fetch",e=>{if(e.request.method!="GET")return;e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(C).then(c=>c.put(e.request,cp));return r}).catch(()=>caches.match(e.request)))});
self.addEventListener("notificationclick",e=>{
 e.notification.close();
 const url=(e.notification.data&&e.notification.data.url)||"./#hw";
 e.waitUntil(clients.matchAll({type:"window",includeUncontrolled:true}).then(l=>{
  for(const c of l){
   if("focus"in c){try{c.postMessage({type:"open",url})}catch(err){}return c.focus()}
  }
  return clients.openWindow(url);
 }));
});

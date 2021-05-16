chrome.runtime.onInstalled.addListener(() => {
    console.log("installed");
})

chrome.bookmarks.onCreated.addListener(()=> {
    alert('bookmark saved');
})

chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
    console.log(tabs[0].url);
});
//export const exec = (command, value = null) => document.execCommand(command, false, value)
const formatBlock = "formatBlock";
function makeBold(sel) {
  document.execCommand("bold");
}
function makeItalic(sel) {
  document.execCommand("italic");
}
function makeUnderlined(sel) {
  document.execCommand("underline");
}
function addH() {
  document.execCommand("formatBlock", false, "h1");
}
function addh() {
  document.execCommand("formatBlock", false, "h2");
}
function unorderedList() {
  document.execCommand("insertUnorderedList");
}
function orderedList() {
  document.execCommand("insertOrderedList");
}
function addLink() {
  const url = window.prompt("Enter the link URL");
  if (url) document.execCommand("createLink", url);
}

const image_input = document.querySelector("#image_input");
$.fn.focusEnd = function() {
  $(this).focus();
  var tmp = $('<span />').appendTo($(this)),
      node = tmp.get(0),
      range = null,
      sel = null;

  if (document.selection) {
      range = document.body.createTextRange();
      range.moveToElementText(node);
      range.select();
  } else if (window.getSelection) {
      range = document.createRange();
      range.selectNode(node);
      sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
  }
  tmp.remove();
  return this;
}
image_input.addEventListener("change", function () {
  var uploaded_image = "";
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    uploaded_image = reader.result;
    if (uploaded_image != "") {
      var div = document.createElement("div");
      div.id = "display_image";
      document.getElementById("textBox").appendChild(div);
      //console.log("New Div is", div);
    }
    document.querySelector(
      "#display_image"
    ).style.backgroundImage = `url(${uploaded_image})`;
  });
  reader.readAsDataURL(this.files[0]);
  //image_input.removeEventListener();
  
  
});
function addCode() {
  doucment.execCommand("formatBlock", false, "<pre>");
}

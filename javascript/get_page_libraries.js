// Code snippets to extract information about page libraries,
// frameworks and styles

// Code snippet to list all CSS libraries for a given page
const styles = document.querySelectorAll("link");
styles.forEach((link) => {
  if (link.rel === "stylesheet") {
    console.log(`${link.getAttribute("href")}`);
  }
});

// Code snippet to list all third party scripts for a given page
// along with integrity hashes if available
const scripts = document.querySelectorAll("script");
scripts.forEach((script) => {
  if (script.src) {
    if (script.integrity) {
      console.log(`${script.src} ${script.integrity}`);
    }
    console.log(`${script.src}`);
  }
});

// Detect version of Ember.js
console.log(Ember.VERSION);

// Detect Angular.js version
console.log(angular.version);

// For Angular v4.0+
const elements = getAllAngularRootElements();
const version = elements[0].attributes["ng-version"];
console.log(version);

// Detect React version
console.log(React.version);

// Detect Vue version
console.log(Vue.version);
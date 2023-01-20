class Person {
    constructor(name, age) {
        this.name = name;
    }

        sayHi() {
            alert("Hello, I'm " + this.name);
    }
}
let p = new Person("Quan");
p.sayHi();
// document.body.innerHTML = "<p>Hello, I'm " + p.name + "</p>";

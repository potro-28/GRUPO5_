const boton = document.getElementById("btn-accesibilidad");
const menus = document.getElementById("menu-accesibilidad");

let fontSize = parseInt(
    localStorage.getItem("fontSize")
) || 16;

document.body.style.fontSize = fontSize + "px"

boton.addEventListener("click", () => {
    menus.classList.toggle("oculto");
});

function aumentarTexto() {

    fontSize += 2;

    document.body.style.fontSize =
        fontSize + "px";

    localStorage.setItem(
        "fontSize",
        fontSize
    );
}

function disminuirTexto() {

    fontSize -= 2;

    if(fontSize < 12){
        fontSize = 12;
    }

    document.body.style.fontSize =
        fontSize + "px";

    localStorage.setItem(
        "fontSize",
        fontSize
    );
}


function alternarContraste() {

    document.body.classList.toggle(
        "alto-contraste"
    );

    localStorage.setItem(
        "contraste",
        document.body.classList.contains(
            "alto-contraste"
        )
    );
}


function escalaGrises() {

    document.body.classList.toggle(
        "escala-grises"
    );

    localStorage.setItem(
        "grises",
        document.body.classList.contains(
            "escala-grises"
        )
    );
}

function resaltarEnlaces() {

    document.body.classList.toggle(
        "resaltar-enlaces"
    );

    localStorage.setItem(
        "enlaces",
        document.body.classList.contains(
            "resaltar-enlaces"
        )
    );
}


let lecturaActual = null;

function leerPagina() {

    speechSynthesis.cancel();

    let texto = document.body.innerText;

    lecturaActual = new SpeechSynthesisUtterance(texto);

    lecturaActual.lang = "es-ES";

    speechSynthesis.speak(lecturaActual);
}

function detenerLectura() {

    speechSynthesis.cancel();

    lecturaActual = null;
}

function restablecerAccesibilidad() {

    localStorage.clear();

    document.body.style.fontSize = "16px";

    document.body.classList.remove(
        "alto-contraste"
    );

    document.body.classList.remove(
        "escala-grises"
    );

    document.body.classList.remove(
        "resaltar-enlaces"
    );
}

window.onload = () => {

    if(localStorage.getItem("contraste") === "true"){
        document.body.classList.add(
            "alto-contraste"
        );
    }

    if(localStorage.getItem("grises") === "true"){
        document.body.classList.add(
            "escala-grises"
        );
    }

    if(localStorage.getItem("enlaces") === "true"){
        document.body.classList.add(
            "resaltar-enlaces"
        );
    }

    if(localStorage.getItem("fontSize")){
        document.body.style.fontSize =
            localStorage.getItem("fontSize") + "px";
    }
};
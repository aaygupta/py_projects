function translate_this() {
    let input_data = document.getElementById('input_data').value
    let source = document.getElementById('source')
    let src_lang = source.options[source.selectedIndex].text
    let destination = document.getElementById('destination')
    let des_lang = destination.options[destination.selectedIndex].text
    eel.translate(input_data, src_lang, des_lang)(setOutput)
}

function setOutput(outputText) {
    document.getElementById('output_data').value = outputText
}
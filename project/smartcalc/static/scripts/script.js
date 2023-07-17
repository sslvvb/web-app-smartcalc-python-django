function appendValue(value, event) {
    event.preventDefault();
    document.getElementById('expression').value += value;
}

function clearExpression(event) {
    event.preventDefault();
    document.getElementById('expression').value = '';
}

function calculateExpression(event) {
    if (document.getElementById('expression').value == '' ||
        document.getElementById('x_num').value == '') {
        event.preventDefault();
    } else {
        indexPostSubmit();
    }
}

function graphExpression(event) {
    const xMin = parseFloat(document.getElementById('x_min').value);
    const xMax = parseFloat(document.getElementById('x_max').value);
    const yMin = parseFloat(document.getElementById('y_min').value);
    const yMax = parseFloat(document.getElementById('y_max').value);
    if (document.getElementById('expression').value != '' &&
        document.getElementById('x_num').value != '' &&
        document.getElementById('x_min').value != '' &&
        document.getElementById('x_max').value != '' &&
        document.getElementById('y_min').value != '' &&
        document.getElementById('y_max').value != '' &&
        xMin < xMax && yMin < yMax && xMin != xMax && yMin != yMax) {
        graphPostSubmit();
    } else {
        event.preventDefault();
    }
}

function indexPostSubmit() {
    const form = document.getElementById('calculator-form');
    form.action = '/';
    form.method = 'POST';
    form.submit();
}

function graphPostSubmit() {
    const form = document.getElementById('calculator-form');
    form.action = 'graph/';
    form.method = 'POST';
    form.submit();
}


function parseHistoryItem(historyItem) {
    historyItem = historyItem.trim();
    var splitLines = historyItem.split('=');
    var data = {
        expression_or_result: splitLines[0].trim(),
        x_value: splitLines[1].trim(),
        history: services.write_history(historyItem)
    };
    return data;
}


// TODO: delete ?  views.py
function historySubmit() {
    const selectElement = document.querySelector('select[name="history"]');
    const selectedOption = selectElement.options[selectElement.selectedIndex].value;

    const historyItem = selectedOption.trim();
    const splitLines = historyItem.split('=');
    const data = {
        expression_or_result: splitLines[0].trim(),
        x_value: splitLines[2].trim(),
    };

    const expressionInput = document.querySelector('.expression-input');
    expressionInput.value = data.expression_or_result;

    // x value also set
    // refactor me pls
}




function cleanHistorySubmit() {
    const form = document.getElementById('calculator-form');
    form.action = 'clean_history/';
    form.method = 'POST';
    form.submit();
}

// TODO: разные формы для этого мб ?
function backgroundSubmit() {
    const form = document.getElementById('calculator-form');
    form.action = 'background/';
    form.method = 'POST';
    form.submit();
}

function colorSubmit() {
    const form = document.getElementById('calculator-form');
    form.action = 'main_color/';
    form.method = 'POST';
    form.submit();
}

function fontSubmit() {
    const form = document.getElementById('calculator-form');
    form.action = 'font_size/';
    form.method = 'POST';
    form.submit();
}

// TODO: для внутренних мб другой гугл стиль ?
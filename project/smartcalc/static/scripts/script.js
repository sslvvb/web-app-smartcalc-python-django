function appendValue(value, event) {
    event.preventDefault();
    document.getElementById('expression').value += value;
}

function clearExpression(event) {
    event.preventDefault();
    document.getElementById('expression').value = '';
}

function evaluateExpression(event) {
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

// TODO: для внутренних мб другой гугл стиль ?

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

// TODO: delete ?  views.py
function historySubmit() {
    // const expressionValue = document.getElementById('history-select').value;
    // console.log(expressionValue);
    // не отправлять запрос, а на стороне фронта просто ставить выражение в поле на страничке
    // const form = document.getElementById('calculator-form');
    const form = document.getElementById('calculator-form');
    form.action = 'history/';
    form.method = 'POST';
    form.submit();
}

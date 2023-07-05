function appendValue(value) {
    document.getElementById('expression').value += value;
}

function clearExpression() {
    document.getElementById('expression').value = '';
}

function evaluateExpression() {  // TODO: избавиться от одинаковых функций
    if (document.getElementById('expression').value != '' &&
        document.getElementById('x_num').value != '') {
        const form = document.getElementById('calculator-form');
        form.action = '/';
        form.method = 'POST';
        form.submit();
    }
}

function historySelect() {
    const form = document.getElementById('calculator-form');
    form.action = '/';
    form.method = 'POST';
    form.submit();
}

function historyClean() {
    const form = document.getElementById('calculator-form');
    form.action = '/';
    form.method = 'POST';
    form.submit();
}

function graphExpression() {
    if (document.getElementById('expression').value != '' &&
        document.getElementById('x_num').value != '' &&
        document.getElementById('x_min').value != '' &&
        document.getElementById('x_max').value != '' &&
        document.getElementById('y_min').value != '' &&
        document.getElementById('y_max').value != '') {
        const form = document.getElementById('calculator-form');
        form.action = 'graph/';
        form.method = 'POST';
        form.submit();
    }
}

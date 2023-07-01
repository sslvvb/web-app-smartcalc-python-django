function appendValue(value) {
    document.getElementById('expression').value += value;
}

function clearExpression() {
    document.getElementById('expression').value = '';
}

function evaluateExpression() {  // TODO: избавиться от одинаковых функций
    const form = document.getElementById('calculator-form');
    form.action = '/';
    form.method = 'POST';
    form.submit();
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
    const form = document.getElementById('calculator-form');
    form.action = 'graph/';
    form.method = 'POST';
    form.submit();
}
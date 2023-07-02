#include "model.h"
#include <iostream> // tmp

// В модель должны быть вынесены все функциональные возможности калькулятора
// таким образом, чтобы в будущем ее можно было использовать без остальных слоев

// Подготовить полное покрытие unit-тестами методов, находящихся в слое модели

#ifdef __cplusplus
extern "C" {
#endif

// надо на string заменить ?
// как обрабатывать если возвращается ошибка ?
double GetResult(const char* expression) {
  s21::Model model;
  return model.GetResult(expression);
}

std::pair<std::vector<double>, std::vector<double>> GetResultForGraph(const char* expression, double x_min, double x_max) {
  std::cout << "start cpp model | str = " << expression << " " << x_min << " " << x_max << std::endl;
  s21::Model model;
  std::cout << "ctor model" << std::endl;
  std::pair<std::vector<double>, std::vector<double>> result = model.GetResultForGraph(expression, x_min, x_max);
  std::cout << "done cpp model" << std::endl;
  return result;
}

std::vector<double> printString(const char* str, double ddd) {
  std::cout << str << ddd << std::endl;
  std::vector<double> res = {1, 2, 3};
  return res;
}

#ifdef __cplusplus
}
#endif

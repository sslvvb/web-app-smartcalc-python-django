#include "model.h"
#include <iostream> // tmp

// В модель должны быть вынесены все функциональные возможности калькулятора
// таким образом, чтобы в будущем ее можно было использовать без остальных слоев

// Подготовить полно е покрытие unit-тестами методов, находящихся в слое модели

#ifdef __cplusplus
extern "C" {
#endif

double GetResult(const char* expression, const char* x_value) {  // надо на string заменить ?
  s21::Model model;
  std::cout << expression << "   wrapper string" << std::endl;
  // перевести х к даблу и отправить в модель
  return model.GetResult(expression); // float возвращать ?
}

#ifdef __cplusplus
}
#endif

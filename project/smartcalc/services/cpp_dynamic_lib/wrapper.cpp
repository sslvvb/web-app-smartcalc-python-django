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

#ifdef __cplusplus
}
#endif

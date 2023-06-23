#include "model.h"
#include <iostream>

// В модель должны быть вынесены все функциональные возможности калькулятора
// таким образом, чтобы в будущем ее можно было использовать без остальных слоев

// Подготовить полное покрытие unit-тестами методов, находящихся в слое модели

#ifdef __cplusplus
extern "C" {
#endif

int tmp(int num) {
  s21::Model model;
  return model.res(num);
}

// double GetResult(const char* str) {  // надо на string заменить ?
double GetResult(std::string str) {  // надо на string заменить ?
  s21::Model model;
  std::cout << str << "wrapper" << std::endl;
  return model.GetResult(str);
}

#ifdef __cplusplus
}
#endif

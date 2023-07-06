#include "model.h"

// Подготовить полное покрытие unit-тестами методов, находящихся в слое модели

#ifdef __cplusplus
extern "C" {
#endif

bool GetResult(const char* expression, double& result) {
  try {
    s21::Model model;
    result = model.GetResult(expression);
    return true;
  } catch (const std::exception&) {
    return false;
  }
}

// style and checks
// как обрабатывать если возвращается ошибка ?
void GetResultForGraph(const char* expression, double x_min, double x_max, int number_of_steps,
                       double* x_buf_values, double* y_buf_values) {
  s21::Model model;
  std::pair<std::vector<double>, std::vector<double>> result = model.GetResultForGraph(expression, x_min, x_max, number_of_steps);
  for (size_t i = 0; i < number_of_steps; i++) {
    x_buf_values[i] = result.first[i];
    y_buf_values[i] = result.second[i];
  }
}

#ifdef __cplusplus
}
#endif

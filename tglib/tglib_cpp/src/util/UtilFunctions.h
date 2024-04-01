/* Copyright (C) 2022 Lutz Oettershagen - All Rights Reserved
 *
 * This file is part of TGLib which is released under MIT license.
 * See file LICENSE.md or go to https://gitlab.com/tgpublic/tglib
 * for full license details.
 */

 /** @file UtilFunctions.h
  *  @brief Helpful utility functions
  */

#ifndef TGLIB_UTILFUNCTIONS_H
#define TGLIB_UTILFUNCTIONS_H

#include <vector>
#include <algorithm>
#include <numeric>
#include <valarray>
#include <chrono>
#include <iostream>
#include <omp.h>

namespace tglib {

	/**
	 * Computes mean and standard deviation.
	 * @tparam T a numerical type
	 * @param values vector of numerical values
	 * @param mean the mean
	 * @param stdev the standard deviation
	 */
	template<typename T>
	void get_mean_std(std::vector<T>& values, double& mean, double& stdev) {
		double sum = std::accumulate(std::begin(values), std::end(values), 0.0);
		mean = sum / values.size();
		double accum = 0.0;
		std::for_each(std::begin(values), std::end(values), [&](const double d) {
			accum += (d - mean) * (d - mean);
			});
		stdev = sqrt(accum / (values.size()));
	}

	template<typename E>
	void merge(std::vector<E>& array, int left, int mid, int right) {
		int n1 = mid - left + 1;
		int n2 = right - mid;

		std::vector<E> leftArray(n1);
		std::vector<E> rightArray(n2);

		for (int i = 0; i < n1; ++i) {
			leftArray[i] = array[left + i];
		}

		for (int j = 0; j < n2; ++j) {
			rightArray[j] = array[mid + 1 + j];
		}

		int i = 0, j = 0, k = left;
		while (i < n1 && j < n2) {
			if (leftArray[i] <= rightArray[j]) {
				array[k] = leftArray[i];
				++i;
			}
			else {
				array[k] = rightArray[j];
				++j;
			}
			++k;
		}

		while (i < n1) {
			array[k] = leftArray[i];
			++i;
			++k;
		}

		while (j < n2) {
			array[k] = rightArray[j];
			++j;
			++k;
		}
	}

	template<typename E>
	void mergeSort(std::vector<E>& array, int left, int right) {
		if (left < right) {
			int mid = left + (right - left) / 2;

#pragma omp parallel sections
			{
#pragma omp section
				{
					mergeSort(array, left, mid);
				}

#pragma omp section
				{
					mergeSort(array, mid + 1, right);
				}
			}

			merge(array, left, mid, right);
		}
	}

} // tglib

#endif //TGLIB_UTILFUNCTIONS_H

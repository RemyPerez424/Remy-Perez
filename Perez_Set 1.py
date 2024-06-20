{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50e90b34-38b3-4aa0-9b3d-8edad8393910",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9e8249e2-ae15-4884-bcba-4d91c04164b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def savings(gross_pay, tax_rate, expenses):\n",
    "    savings = (((1-tax_rate)*gross_pay)//1) - expenses\n",
    "    return savings "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "9e59e55e-eaa5-431b-ba9b-f405206e44a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def material_waste(total_material, material_units, num_jobs, job_consumption):\n",
    "    material_waste = str(total_material - (num_jobs*job_consumption)) + material_units\n",
    "    return material_waste"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8a53b0ca-b55e-4976-9c81-de6e96cfa3ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "def interest(principal, rate, periods):\n",
    "    interest = (principal + (principal*(rate*periods)))//1\n",
    "    return interest"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "239bf848-0d79-41f9-bcb1-92d31444d08b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

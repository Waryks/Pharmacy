class MedicineValidator:
    def validate(self, medicine):

        errors = []
        if medicine.getPrescription() not in ["True", "False"]:
            errors.append("Program: The prescription can only be True or False")

        if errors:
            raise ValueError(errors)

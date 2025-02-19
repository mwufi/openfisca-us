from openfisca_us.model_api import *


class ny_itemized_deductions_max(Variable):
    value_type = float
    entity = TaxUnit
    label = "NY uncapped itemized deductions"
    unit = USD
    definition_period = YEAR
    reference = "https://www.nysenate.gov/legislation/laws/TAX/615"
    defined_for = StateCode.NY

    def formula(tax_unit, period, parameters):
        gov = parameters(period).gov
        federal_deductions_if_itemizing = (
            gov.irs.deductions.deductions_if_itemizing
        )
        federal_deductions_if_itemizing = [
            deduction
            for deduction in federal_deductions_if_itemizing
            if deduction
            not in [
                "salt_deduction",
                "qualified_business_income_deduction",
            ]
        ]
        return add(tax_unit, period, federal_deductions_if_itemizing)

from openfisca_us.model_api import *


class ny_itemized_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "NY itemized deductions"
    unit = USD
    definition_period = YEAR
    reference = "https://www.nysenate.gov/legislation/laws/TAX/615"
    defined_for = StateCode.NY

    def formula(tax_unit, period, parameters):
        max_deductions = tax_unit("ny_itemized_deductions_max", period)
        reduction = tax_unit("ny_itemized_deductions_reduction", period)
        # There are some other specific details about some types of itemized deductions
        # likely non-modellable in the CPS. Requires further investigation.
        return max_deductions - reduction

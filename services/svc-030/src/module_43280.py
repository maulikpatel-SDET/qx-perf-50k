"""Service module 43280: business logic, no crypto."""


def calculate_total_43280(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43280():
    return 'module 43280 handles orders and invoices'

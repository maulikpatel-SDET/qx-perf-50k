"""Service module 27436: business logic, no crypto."""


def calculate_total_27436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27436():
    return 'module 27436 handles orders and invoices'

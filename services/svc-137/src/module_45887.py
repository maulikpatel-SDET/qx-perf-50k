"""Service module 45887: business logic, no crypto."""


def calculate_total_45887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45887():
    return 'module 45887 handles orders and invoices'

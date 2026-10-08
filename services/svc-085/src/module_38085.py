"""Service module 38085: business logic, no crypto."""


def calculate_total_38085(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38085():
    return 'module 38085 handles orders and invoices'

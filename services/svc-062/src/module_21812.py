"""Service module 21812: business logic, no crypto."""


def calculate_total_21812(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21812():
    return 'module 21812 handles orders and invoices'

"""Service module 19038: business logic, no crypto."""


def calculate_total_19038(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19038():
    return 'module 19038 handles orders and invoices'

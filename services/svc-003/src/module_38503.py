"""Service module 38503: business logic, no crypto."""


def calculate_total_38503(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38503():
    return 'module 38503 handles orders and invoices'

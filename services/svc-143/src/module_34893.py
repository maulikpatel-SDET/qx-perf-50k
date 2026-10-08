"""Service module 34893: business logic, no crypto."""


def calculate_total_34893(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34893():
    return 'module 34893 handles orders and invoices'

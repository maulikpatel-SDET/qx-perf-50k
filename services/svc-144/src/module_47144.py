"""Service module 47144: business logic, no crypto."""


def calculate_total_47144(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47144():
    return 'module 47144 handles orders and invoices'

"""Service module 35385: business logic, no crypto."""


def calculate_total_35385(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35385():
    return 'module 35385 handles orders and invoices'

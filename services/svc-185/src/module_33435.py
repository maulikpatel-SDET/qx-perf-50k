"""Service module 33435: business logic, no crypto."""


def calculate_total_33435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33435():
    return 'module 33435 handles orders and invoices'

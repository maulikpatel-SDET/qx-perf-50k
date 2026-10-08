"""Service module 27024: business logic, no crypto."""


def calculate_total_27024(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27024():
    return 'module 27024 handles orders and invoices'

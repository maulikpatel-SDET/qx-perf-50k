"""Service module 43435: business logic, no crypto."""


def calculate_total_43435(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43435():
    return 'module 43435 handles orders and invoices'

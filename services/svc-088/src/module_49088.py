"""Service module 49088: business logic, no crypto."""


def calculate_total_49088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49088():
    return 'module 49088 handles orders and invoices'

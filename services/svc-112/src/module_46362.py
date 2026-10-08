"""Service module 46362: business logic, no crypto."""


def calculate_total_46362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46362():
    return 'module 46362 handles orders and invoices'

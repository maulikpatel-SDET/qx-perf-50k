"""Service module 21362: business logic, no crypto."""


def calculate_total_21362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21362():
    return 'module 21362 handles orders and invoices'

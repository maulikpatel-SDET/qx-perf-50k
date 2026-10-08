"""Service module 36362: business logic, no crypto."""


def calculate_total_36362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36362():
    return 'module 36362 handles orders and invoices'

"""Service module 34071: business logic, no crypto."""


def calculate_total_34071(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34071():
    return 'module 34071 handles orders and invoices'

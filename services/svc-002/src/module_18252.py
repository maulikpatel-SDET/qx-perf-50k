"""Service module 18252: business logic, no crypto."""


def calculate_total_18252(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18252():
    return 'module 18252 handles orders and invoices'

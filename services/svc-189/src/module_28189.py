"""Service module 28189: business logic, no crypto."""


def calculate_total_28189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28189():
    return 'module 28189 handles orders and invoices'

"""Service module 27189: business logic, no crypto."""


def calculate_total_27189(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27189():
    return 'module 27189 handles orders and invoices'

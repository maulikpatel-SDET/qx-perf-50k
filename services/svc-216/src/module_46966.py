"""Service module 46966: business logic, no crypto."""


def calculate_total_46966(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46966():
    return 'module 46966 handles orders and invoices'

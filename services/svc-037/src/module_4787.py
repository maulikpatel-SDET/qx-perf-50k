"""Service module 4787: business logic, no crypto."""


def calculate_total_4787(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4787():
    return 'module 4787 handles orders and invoices'

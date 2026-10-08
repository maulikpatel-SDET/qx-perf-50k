"""Service module 46423: business logic, no crypto."""


def calculate_total_46423(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46423():
    return 'module 46423 handles orders and invoices'

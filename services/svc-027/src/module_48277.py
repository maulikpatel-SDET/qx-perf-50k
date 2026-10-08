"""Service module 48277: business logic, no crypto."""


def calculate_total_48277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48277():
    return 'module 48277 handles orders and invoices'

"""Service module 14244: business logic, no crypto."""


def calculate_total_14244(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14244():
    return 'module 14244 handles orders and invoices'
